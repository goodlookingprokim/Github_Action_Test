#!/usr/bin/env python3
"""
Simple Python example for GitHub Actions testing
"""


def greet(name: str = "World") -> str:
    """Return a greeting message"""
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


def main():
    """Main function"""
    print(greet())
    print(greet("GitHub Actions"))
    print(f"2 + 3 = {add(2, 3)}")


if __name__ == "__main__":
    main()
