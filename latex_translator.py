from __future__ import annotations
import re
from dataclasses import dataclass, field
from typing import Callable

@dataclass(frozen=True)
class Ok:
    value: str

@dataclass(frozen=True)
class Err:
    error: str
    original: str

Result = Ok | Err
Transform = Callable[[str], Result]


def compose(*transforms: Transform) -> Transform:
    def composed(s: str) -> Result:
        result: Result = Ok(s)
        for t in transforms:
            match result:
                case Ok(v): result = t(v)
                case Err(): return result
        return result
    return composed


def fix_sqrt_parens(s: str) -> Result:
    prev, current = "", s
    while prev != current:
        prev = current
        out: list[str] = []
        i = 0
        while i < len(current):
            if current[i:i+6] == "\\sqrt(":
                out.append("\\sqrt{")
                i += 6
                depth, start = 1, i
                while i < len(current) and depth > 0:
                    if current[i] == "(": depth += 1
                    elif current[i] == ")": depth -= 1
                    if depth > 0: i += 1
                if depth != 0:
                    return Err("Unmatched paren in sqrt()", current)
                out.append(current[start:i])
                out.append("}")
                i += 1
            else:
                out.append(current[i])
                i += 1
        current = "".join(out)
    return Ok(current)


def fix_text_with_math(s: str) -> Result:
    def replace(m: re.Match[str]) -> str:
        content = m.group(1)
        if "$" not in content:
            return m.group(0)
        parts: list[str] = []
        remaining = content
        while "$" in remaining:
            dm = re.search(r'\$([^$]*)\$', remaining)
            if not dm: break
            before = remaining[:dm.start()]
            if before: parts.append(f"\\text{{{before}}}")
            math = dm.group(1).strip()
            if math: parts.append(math)
            remaining = remaining[dm.end():]
        if remaining: parts.append(f"\\text{{{remaining}}}")
        return "".join(parts) if parts else ""
    return Ok(re.sub(r'\\text\{([^}]*)\}', replace, s))


def remove_embedded_emoji(s: str) -> Result:
    return Ok(re.sub(r'!\[[^\]]*\]\(\./images/smilies/[^)]+\)', '', s))


def fix_currency(s: str) -> Result:
    # $1234 or $1,234 in text context -> \$1234 (escape the dollar)
    # Match: $ followed by digits (with optional commas/decimals), not followed by math-like chars
    return Ok(re.sub(r'\$(\d[\d,]*(?:\.\d{2})?)\b(?![_^{\\])', r'\\$\1', s))


def fix_escaped_triple_dollar(s: str) -> Result:
    # \$$$ at end of line is often \$ (escaped) + $$ (display close) that got mangled
    # Keep the $$ but remove the escaped dollar before it
    return Ok(re.sub(r'\\\$\$\$', '$$', s))


def normalize_delimiters(s: str) -> Result:
    r = s.replace("\\[", "$$").replace("\\]", "$$")
    r = r.replace("\\(", "$").replace("\\)", "$")
    r = r.replace("[$]", "$").replace("[$ ]", "$")
    return Ok(r)


def fix_missing_space_before_math(s: str) -> Result:
    # "word$X$" -> "word $X$" (add space before inline math)
    return Ok(re.sub(r'([a-zA-Z])\$([A-Za-z\\])', r'\1 $\2', s))


def fix_standalone_dollar(s: str) -> Result:
    def fix_line(line: str) -> str:
        stripped = line.strip()
        if stripped == "$":
            return "$$"
        # Handle blockquote: "> $" -> "> $$"
        if stripped == "> $":
            return line.replace("> $", "> $$")
        return line
    return Ok("\n".join(fix_line(line) for line in s.split("\n")))


def fix_trailing_double_dollar(s: str) -> Result:
    return Ok(re.sub(r'\$ \$\s*$', '$', s, flags=re.MULTILINE))


def fix_mixed_display_delimiters(s: str) -> Result:
    def fix(line: str) -> str:
        st = line.strip()
        if st.startswith("$$") and not st.startswith("$$$"):
            m = re.search(r'(\$+)\s*$', st)
            if m and m.group(1) == "$":
                return line.rstrip().rstrip("$") + "$$"
        return line
    return Ok("\n".join(fix(line) for line in s.split("\n")))


def validate_balanced_dollars(s: str) -> Result:
    # Remove escaped \$ before counting
    t = re.sub(r'\\\$', '', s)
    display = t.count("$$")
    if display % 2 != 0:
        return Err(f"Unbalanced $$: {display}", s)
    inline = t.replace("$$", "").count("$")
    if inline % 2 != 0:
        return Err(f"Unbalanced $: {inline}", s)
    return Ok(s)


def validate_no_text_with_dollar(s: str) -> Result:
    if re.search(r'\\text\{[^}]*\$', s):
        return Err("$ inside text{}", s)
    return Ok(s)


def validate_no_sqrt_parens(s: str) -> Result:
    if "\\sqrt(" in s:
        return Err("sqrt() not converted", s)
    return Ok(s)


transform_pipeline: Transform = compose(
    fix_sqrt_parens,
    fix_text_with_math,
    remove_embedded_emoji,
    fix_currency,
    fix_escaped_triple_dollar,
    normalize_delimiters,
    fix_standalone_dollar,
    fix_trailing_double_dollar,
    fix_mixed_display_delimiters,
    fix_missing_space_before_math,
)

validate_pipeline: Transform = compose(
    validate_no_text_with_dollar,
    validate_no_sqrt_parens,
    validate_balanced_dollars,
)


def translate(latex: str) -> Result:
    result = transform_pipeline(latex)
    match result:
        case Ok(v): return validate_pipeline(v)
        case Err(): return result


if __name__ == "__main__":
    tests = [
        (r"\sqrt(x+y)", r"\sqrt{x+y}"),
        (r"\sqrt(\Delta t)", r"\sqrt{\Delta t}"),
        (r"\sqrt(a+\sqrt(b))", r"\sqrt{a+\sqrt{b}}"),
        (r"\text{$\sigma$dz}", r"\sigma\text{dz}"),
        (r"\text{foo}", r"\text{foo}"),
        (r"[$]x^2[$]", r"$x^2$"),
        (r"\(x^2\)", r"$x^2$"),
        (r"\[x^2\]", r"$$x^2$$"),
        ("$\nx^2\n$", "$$\nx^2\n$$"),
        # currency
        ("costs $2700 to", r"costs \$2700 to"),
        ("from $100,000", r"from \$100,000"),
    ]
    passed = failed = 0
    for inp, exp in tests:
        match translate(inp):
            case Ok(v) if v == exp: passed += 1; print(f"PASS: {inp!r}")
            case Ok(v): failed += 1; print(f"FAIL: {inp!r} -> {v!r} (expected {exp!r})")
            case Err(e, _): failed += 1; print(f"FAIL: {inp!r} -> error: {e}")
    print(f"\n{passed}/{passed+failed} passed")
