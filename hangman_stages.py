stages=[
r'''
+--------+
    |    |
    O    |
   \|/   |
   / \   |
+--------+

''',
r'''
+--------+
    |    |
    O    |
   \|/   |
   /     |
+--------+

''',r'''
+--------+
    |    |
    O    |
   \|/   |
         |
+--------+

''',r'''
+--------+
    |    |
    O    |
   \|    |
         |
+--------+
''',r'''
+--------+
    |    |
    O    |
    |    |
         |
+--------+
''',r'''
+--------+
    |    |
    O    |
         |
         |
+--------+
''',r'''
+--------+
    |    |
         |
         |
         |
+--------+
'''
]
if __name__=="main":
    print(stages[3])
    print(stages[2])
    print(stages[4])