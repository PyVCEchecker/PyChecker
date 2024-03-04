"""
Playing around with applicatives
"""
from functools import reduce


class Result(object):
    pass


class Success(Result):
    def __init__(self, value):
        self.value = value

    def apply(self, fx):
        a = 10
        return fx.map(self.value)

    def map(self, f):
        return Success(f(self.value))

    def bind(self, f):
        return f(self.value)

    def __str__(self):
        return 'Success<{}>'.format(self.value)


class Failure(Result):
    def __init__(self, err):
        self.error = err

    def map(self, f):
        return Failure(self.error)

    def bind(self, f):
        return Failure(self.error)

    def __str__(self):
        return 'Failure<{}>'.format(self.error)

    def apply(self, fx):
        if isinstance(fx, Failure):
            return Failure(self.error + fx.error)
        else:
            return self



def success(x):
    return Success(x)


def applyy(rf, rv):
    if isinstance(rf, Success) and isinstance(rv, Success):
        return rf.value(rv.value)
    elif isinstance(rf, Failure) and isinstance(rv, Failure):
        return Failure(rf.error + rv.error)
    elif isinstance(rf, Failure):
        return rf
    else:
        return rv


def bind(x, f):
    if isinstance(x, Success):
        return f(x.value)
    else:
        return x


def bindf(f):
    def inner(x):
        if isinstance(x, Success):
            return f(x.value)
        else:
            return x
    return success(inner)


def map(x, f):
    return bind(x, comp(f, success))


def comp(*funcs):
    def inner(x):
        return reduce(lambda acc, f: f(acc), funcs, x)
    return inner


def create_id(customer_id):
    if customer_id > 0:
        return success(customer_id)
    else:
        return Failure(['Customer id must be positive'])

def create_email(email):
    if '@' not in email:
        return Failure(['Must be email address'])
    else:
        return Success(email)


def is_upper(name):
    return (success(name)
            if name == name.upper()
            else Failure(['Must be uppercase']))

def not_none(name):
    return success(name) if name else Failure(["Name cannot be empty"])


def validate_person(name, email):
    r_name = create_id(name)
    r_email = create_email(email)
    return applyy(map(r_name, make_person), r_email)

def lift2(f, r1, r2):
    return r1.map(f).apply(r2)


def make_person(name):
    def _make_person(email):
        return {'person': name, 'email': email}
    return _make_person




r1 = bind(success(10), lambda x: success(x + 100))
r2 = (lambda x: success(x + 100))(10)

print(r1, r2)

# print(validate_person(-1, 'nameemail.com'))
print(lift2(make_person, create_id(2), create_email('name@email.com')))


# print(applyy(bindf(is_upper), success("bob")))




# print(Success(lambda x: x + 100).apply(success(10)))


# print(comp(int, lambda x: x + 1, str)("100"))
#
# print(map(success(100), lambda x: x + 100))
#
# print(
#     Success(10)
#         .map(lambda x: x + 1)
#         .bind(lambda x: Success(x + 1))
#         .bind(lambda x: Failure(Exception("FUCK!!!")))
#         .map(lambda x: x + 100)
#
# )