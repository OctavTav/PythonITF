"""
Behavioral Design Patterns (comportamentale)

Chain of responasibility
Command
Interpreter

Iterator = practic este un design pattern care ne permite sa iteam peste anumite colectii / range-uri
    (for si while). Ideea de baza este de a putea accesa in ordine secventiala elementele unei colectii
    fara a cunoaste detalii despre implementarea acestora
    In Python, iteratori sunt implementati folosing o interfata Iterable

Mediator
Memento
Null Object => None, folosit pentru a avea un element comun care sa semnifice absenta unei valori

Observer = permite unei clase Observer sa se "ataseze: de o clasa Subject, pentru ca mai apoi Observer-ul
    sa fie notificat de anumite modificari survenite in Subject
    Ex.: avem User (Observer) si avem Blog (Subject), iar un User vrea sa fie  notificat atunci cand
    pe Blog apare un nou BlogPost

State
Strategy
Template method
Visitor
"""


class Blog:

    def __init__(self, name):
        self.name = name
        self.observers = []

    def add_observer(self, obs):
        # subscribe
        self.observers.append(obs)

    def remove_observer(self, obs):
        # unsubscribe
        self.observers.remove(obs)

    def notify(self):
        # notify, va fi de obicei apelata intern, in fucntie de setari/preferinte (ex cand se adauga un nou BlogPost
        for obs in self.observers:
            obs.notify(self.name)


class User:

    def __init__(self, name,email):
        self.name = name
        self.email = email

    def notify(self, blog_name):
        print(f"Notifying {self.name} about new blog post on {blog_name}")
        # aici de ex am putea trimite un email


blog = Blog("IT Factory Blog")
u1 = User('Ion Popescu', 'ceva@ceva.com')
u2 = User('Maria', '1234@yahoo.com')
u3 = User('Gheo', 'gheo@gmail.com')

# 2 useri fac subscribe
blog.add_observer(u1)
blog.add_observer(u2)
print('-' * 40)
# apare un blog post nou
blog.notify()
print('-' * 40)
blog.remove_observer(u1)

