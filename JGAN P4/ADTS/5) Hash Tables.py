# MAK didn't even mention this so I'm not even gonna bother writing comments for this

def create_hashtabe(size):
    return [None]*size

def hash_function(key,size):
    return len(key) % size  # returns remainder

def insert_into_hashtable(hashtable,key):
    index = hash_function(key, len(hashtable))

    if hashtable[index] is None:
        hashtable[index] = [key]
    else:
        hashtable[index].append(key)

def lookup_in_hashtable(hashtable,key):
    index = hash_function(key, len(hashtable))
    if hashtable[index] is not None:
        return key in hashtable[index]
    return False


# Example usuage
size_of_hashtable = 10
my_hashtabe = create_hashtabe(size_of_hashtable)

insert_into_hashtable(my_hashtabe,"Alice")
insert_into_hashtable(my_hashtabe,"Bob")
print(my_hashtabe)

lookup_name = "Bob"
found = lookup_in_hashtable(my_hashtabe,lookup_name)
print(found)