#!/usr/bin/env python3
"""
Tests for hello.py
"""

import sys
import os

# Add current directory to path to import hello
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from hello import greet, add


def test_greet():
    """Test the greet function"""
    assert greet() == "Hello, World!"
    assert greet("Test") == "Hello, Test!"
    print("✓ greet() tests passed")


def test_add():
    """Test the add function"""
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
    print("✓ add() tests passed")


def main():
    """Run all tests"""
    print("Running Python tests...")
    test_greet()
    test_add()
    print("All Python tests passed! 🎉")


if __name__ == "__main__":
    main()
