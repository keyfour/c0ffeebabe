#!/usr/bin/env python3
#
# Copyright (c) 2018 Alexander Karpov <keyfour13@gmail.com>
#
import sys
import unittest
sys.path.append('../')

import c0ffeebabe


class TestFindCollisionMethods(unittest.TestCase):

    def test_find_substrings(self):
        self.assertEqual(c0ffeebabe.find_substrings("aaaa","aaaa", len("aaaa")), True)
        self.assertEqual(c0ffeebabe.find_substrings("aaaa","bbbb", len("aaaa")), False)

    def test_find_collisions(self):
        self.assertEqual(c0ffeebabe.find_collisions("aaaa", "aaaa", len("aaaa")), len("aaaa"))
        self.assertEqual(c0ffeebabe.find_collisions("aaaa", "bbbb", len("aaaa")), 0)
        self.assertEqual(c0ffeebabe.find_collisions("aaaa", "aabb", 2), 2)
        self.assertEqual(c0ffeebabe.find_collisions("aaaa", "abaa", 2), 2)
        self.assertEqual(c0ffeebabe.find_collisions("aaaa", "baaa",3), 3)