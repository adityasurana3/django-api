class Base:
    permission_class = 'AllowAny'
    
    def get_permission(self):
        return self.permission_class
    
class Child(Base):
    
    def get_permission(self):
        self.permission_class = 'Add'
        return super().get_permission()
    
# b = Base()
# print(b.get_permission())

c = Child()
print(c.permission_class)
print(c.get_permission())
