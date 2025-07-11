from dataclasses import dataclass

@dataclass()
class User:
    name: str
    age: int
    gender: any
    def __str__(self):
        return f"{self.__class__.__name__}: (name: {self.name}, age: {self.age})"

def create_user():
    user_1 = User(name='Jon', age=19, gender='man')
    print(vars(user_1))
    print(user_1)
    print(user_1.name)

def test_args(name, age, *args):
    print(name, age, args)

test_args("Mikhail", 17, "sotnikovme@gmail.com", "men")
create_user()
