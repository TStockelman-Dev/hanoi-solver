# Hanoi Solver

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

# Introduction

The Tower of Hanoi is a famous puzzle dating back to 1883 and invented by a French mathematician named Édouard Lucas. The puzzle consists of a number of disks(n) that sit upon the first of 3 towers. The goal of the puzzle is to move each of the disks from tbe first tower to the third tower by following only 2 rules:

<ol>
  <li>Only one disk may be moved at a time.</li>
  <li>A larger disk cannot be placed on a smaller disk.</li>
</ol>

These two rules create a scenario in which the optimal solution to the puzzle requires exactly 2^n - 1 moves, where n represents the number of starting disks. This provides a minimum exponential time complexity of O(2^n). Furthermore, the solution to the Tower of Hanoi will always follow a set pattern that is dependent on only two factors:

<ol>
  <li>The number of starting disks.</li>
  <li>Whether the current move is even or odd.</li>
</ol>

Understanding these two factors is vital to understanding the iterative solution to the Tower of Hanoi that is seen in this Hanoi Solver, as these patterns are used to identify which specific move should be made at any given moment to complete the puzzle in the optimal number of moves.

# The Iterative Solution

This project began as a certification project that I completed for the freeCodeCamp Python certification course which I later improved upon. While a recursive solution to the Tower of Hanoi algorithm is the typical solution used to resolve this problem, it suffers from a couple of major weaknesses:

<ol>
  <li>A high space complexity which is inefficient for more than a small number of disks and which may lead to a stack overflow for a larger number of disks, despite taking up less space than an iterative solution. Function calls can be slower than iterative solutions to problems, and would likely be the case here.</li>
  <li>The eventual risk of hitting a RecursionError as the number of disks increase. Since iterative solutions like the one used in this project often use a while loop to calculate the moves that need to be made, it can theoretically handle any number of disks.</li>
</ol>

In addition to these factors, I also chose an iterative solution to this project because I understand iteration to be one of my personal strengths. With these things It is with these things in mind that I began looking for an iterative algorithm that would solve the Tower of Hanoi.I spent 2 days studying the optimal solution to the Tower of Hanoi and looking for patterns. After solving the Tower of Hanoi with various number of disks between 1 and 7, I discovered that they key to an iterative solution to the Tower of Hanoi in the optimal number of moves (2^n - 1) lies in the smallest disk. I discovered two principles that, together, could tell me where the smallest disk is on any move given only the move number and the number of starting disks.

<ol>
  <li>The smallest disk will only move on odd-numbered moves, and will <strong>never</strong> move on even-numbered moves. Breaking this rule results in a sub-optimal solution to the Tower of Hanoi and an increase in its time complexity.</li>
  <li>If the number of starting disks is even, the smallest disk will move clockwise on every odd-numbered move. In other words, it will always move from Tower 1 to Tower 2, from Tower 2 to Tower 3, and from Tower 3 to Tower 1 on each odd-numbered move if the number of starting disks is even. If the number of starting disks is odd, the smallest disk will still always move only on odd-numbered moves, but it will move counter-clockwise instead of clockwise.</li>
</ol>

Because of these two principles, I realized that there was only one possible move on any even-numbered move. The fact that the smallest disk only moves on odd-numbered moves, and given that the smallest disk will always be the top disk on the tower that contains it means that nothing will move from the tower that contains the smallest disk on any even numbered move. Since this only leaves two towers between which disks can move on even-numbered moves, and given that each disk is a different size, it follows that there is only one legal move on any even-numbered turn.

This iterative solution is programmed to move the smallest disk according to its fixed pattern on every odd-numbered move, and to take the only legal remaining move on every even-numbered move. Thus, this solution will always solve the Tower of Hanoi in the optimal number of moves given any number of disks.

# Tech Stack and Coding Environments

This project was coded in Python. This was initially coded in the coding environment on the fCC website in order to allow them to run tests on the code to ensure that it works as intended. After passing all of the tests, I continued to work and improve on the code using VS Code. Future updates will involve additional libraries to improve upon this project further.

# Versions and Planned Updates

Version 1.0--Current Version

Planned updates include:
<ul>
  <li>A user interface to make the hanoi-solver more user-friendly.</li>
  <li>Visuals to show the solution to the Tower of Hanoi in real time.</li>
  <li>Improvements to the iterative code to improve the space complexity of this solution.</li>
</ul>

# Who Can Use This Code

Anyone is free to use and improve upon this code, or to use it in their own projects. If you can find a use for my code, I would be overjoyed to see it put to good use in your project.
