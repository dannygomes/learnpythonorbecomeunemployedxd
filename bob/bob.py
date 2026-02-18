def response(hey_bob: str) -> str:
    stripped_bob = hey_bob.strip()
        
    if stripped_bob.endswith("?") and hey_bob.isupper():
        return "Calm down, I know what I'm doing!"
    if stripped_bob.isupper() and not hey_bob.endswith("?"):
        return "Whoa, chill out!"
    if stripped_bob.endswith("?"):
        return "Sure."
    if not stripped_bob:
        return "Fine. Be that way!"

    return "Whatever."