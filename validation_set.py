# imports
import sys

import requests, json, random

# THE DATA
request_data = {1,2,3,4,5,10,11,12,14,18,19,20,25,26,27,28,31,32,33,34,35,38,40,41,44,45,46,48,50,51,52,55,56,57,
                60,63,64,65,67,68,71,72,73,74,75,80,81,85,86,87,90,92,93,95,99,100}


# Defining main function
def main():
    user_id = 10
    auth = {'Authorization': 'token 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'}

    #print(len(request_data))
    n = 50
    total = 0

    for i in range(5):
        total = total + repeat_test(n, auth)
        print("total: " + str(total))

    print()
    print(total/5)

    #user_exists = check_random_user(auth)
    #print(does_user_exist(125413000, auth)) # 125414 errors because it is past total
    #print(user_exists)


def repeat_test(n, auth):
    marked_recaptured = mark_and_recapture_n(n, auth)
    print("marked_recaptured: " + str(marked_recaptured))
    return get_population(n, marked_recaptured)


def get_population(n, marked_recaptured):
    return ((n)*(n)/(marked_recaptured))
    #return (n*marked_recaptured)/n

def mark_and_recapture_n(n, auth):
    first_set = set()
    second_set = set()

    # get the initial n set
    while len(first_set) < n: # set is smaller than n
        random_user = get_random_user(auth)
        if random_user != -1:
            first_set.add(random_user)

    # get the second n set
    while len(second_set) < n: # set is smaller than n
        random_user = get_random_user(auth)
        if random_user != -1:
            second_set.add(random_user)

    # make the union of the sets and get the size of it
    overlap_set = first_set.intersection(second_set)
    return len(overlap_set)

def get_random_user(auth):
    user_id = random.randint(0, 100) # what should this range be?

    if does_user_exist(user_id, auth):
        return user_id
    else:
        return -1
def does_user_exist(user_id, auth):
    """
    response = requests.get('https://api.github.com/users?since=' + str(user_id-1), headers=auth)
    data = response.json()

    #print(len(data))
    #print(data)
    if len(data) == 0:
        return False

    #get the first dictionary entry
    user = data[0]
    #and get the id from that
    found_id = user["id"]
    #print(type(found_id))
    print("found id: " + str(found_id) + ", user id: " + str(user_id))

    """
    if user_id in request_data:
        return True
    else:
        return False


# Using the special variable
# __name__
if __name__ == "__main__":
    main()



