# imports
import sys

import requests, json, random


# Defining main function
def main():
    user_id = 14
    auth = {'Authorization': 'token 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'}
    n = 10

    print("Overlap:" + str(mark_and_recapture_n(n, auth)))
    print("Group sizes: " + str(n))

    #user_exists = check_random_user(auth)
    #print(does_user_exist(125413000, auth)) # 125414 errors because it is past total
    #print(user_exists)


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
    user_id = random.randint(0, 125413000) # what should this range be?

    if does_user_exist(user_id, auth):
        return user_id
    else:
        return -1
def does_user_exist(user_id, auth):
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

    if found_id == user_id:
        return True
    else:
        return False


# Using the special variable
# __name__
if __name__ == "__main__":
    main()




