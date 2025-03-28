from data_structures.stack import execute

def test_stack():
    assert execute(['push 1', 'peek', 'push 4', 'pop', 'peek']) == [1]
    assert execute(['push 8', 'push 2', 'push 3', "peek", 'pop']) == [8, 2]