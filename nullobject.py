
class bst_null():
    """Null object Pattern Implementation"""
    def null_check(self,root):
        if root.isNone():
            return True
        return False
