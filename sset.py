#!/usr/bin/env python3

from typing import List

class SuffixTreeNode:
    def __init__(self):
        self.children = {}
        self.word_indexes = []

class SuffixTree:
    def __init__(self):
        self.root = SuffixTreeNode()

    def insert_suffix(self, suffix: str, word_index: int):
        node = self.root
        for char in suffix:
            if char not in node.children:
                node.children[char] = SuffixTreeNode()
            node = node.children[char]
            if word_index not in node.word_indexes:
                node.word_indexes.append(word_index)

    def build_suffix_tree(self, word: str, word_index: int):
        print(f"Building suffix tree for word: {word}, at index: {word_index}")  # Debug print
        for i in range(len(word)):
            self.insert_suffix(word[i:], word_index)

    def search(self, substring: str) -> List[int]:
        print(f"Searching for substring: {substring}")  # Debug print
        node = self.root
        for char in substring:
            if char not in node.children:
                return []
            node = node.children[char]
        print(f"Found word indexes: {node.word_indexes}")  # Debug print
        return node.word_indexes

class SSet:
    def __init__(self, fname: str) -> None:
        self.fname = fname
        self.words = []
        self.tree = SuffixTree()

    def load(self) -> None:
        with open(self.fname, 'r') as f:
            self.words = [line.rstrip() for line in f]
        print(f"Loaded words: {self.words[:10]}")  # Debug print
        for index, word in enumerate(self.words):
            self.tree.build_suffix_tree(word, index)

    def search(self, substring: str) -> List[str]:
        result_indexes = self.tree.search(substring)
        results = [self.words[i] for i in result_indexes]
        print(f"Search results for substring '{substring}': {results}")  # Debug print
        return results
