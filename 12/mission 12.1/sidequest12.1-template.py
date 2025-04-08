#
# CS1010X --- Programming Methodology
#
# Sidequest 12.1 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

import json

# Reading json file
def read_json(filename):
    """
    Reads a json file and returns a list of modules
    To find out more about json, please google ;)

    For example, cs1010x-fbdata.json contains:

    {
       "members": {
          "data": [
             {
                "name": "Aadit Kamat",
                "id": "1003982836283025"
             },
             {
                "name": "Rakshit Gogia",
                "id": "10204299775189027"
             },
             ...
          ]
       },
       "description": "This is the official FB Group for ...",
       "name": "CS1010X",
       "feed": {
          "data": [
             {
                "message": "Might be useful for the business analytics ...",
                "from": {
                   "name": "Ben Leong",
                   "id": "10152805891837166"
                },
                "name": "Machine Learning with Python - BDU"
                "id": "409054432560329_1002582839874149",
                "likes": {
                   "data": [
                      {
                         "id": "10208170707289199",
                         "name": "Lim Kian Hwee"
                      },
                      {
                         "id": "10204292869386114",
                         "name": "Siidheesh Theivasigamani"
                      },
                      ...
                   ]
                },
                ...
             },
             ...
          ]
       },
       "id": "409054432560329"
    }

    """
    datafile = open(filename, 'r',  encoding='utf-8')
    return json.loads(datafile.read())

# CS1010X Facebook Group Data as a dictionary object
fb_data = read_json('cs1010x-fbdata.json')

##########
# Task a #
##########

def count_comments(data):
    # Returns the total number of comments
    i = 0
    for item in data["feed"]["data"]:
        if("comments" in item):
            i += len(item["comments"]["data"])
    return i

#print("Number of Comments in CS1010X: ", count_comments(fb_data))

##########
# Task b #
##########

def count_likes(data):
    # Returns the total number of likes (in feed posts and comments)
    i = 0
    for item in data["feed"]["data"]:
        if("likes" in item):
            i += len(item["likes"]["data"])
        if("comments" in item):
            for comment in item["comments"]["data"]:
                i += comment["like_count"]     
    return i

#print("Number of Likes in CS1010X: ", count_likes(fb_data))

##########
# Task c #
##########

def create_member_dict(data):
    # Lookup table where key is id and value is member data object
    dic = {}

    for person in data["members"]["data"]:
        sub_dic = {}
        for item in person:
            if(item != "id"):
                sub_dic[item] = person[item]
        dic[person["id"]] = sub_dic

    return dic
    

member_dict = create_member_dict(fb_data)
#print(member_dict["10205702832196255"])

# Q: Why did we choose the id of the member data object to be the key?
# A: Some people may have the same name which would cause the key values to clash in the dictionary. Their IDs, however, are always unique

# Q: It is inappropriate to use the name as the key. What will happen if we use the name as the key of member_dict?
# A: If a duplicate name is inserted into the dictionary, it will overwrite the data associated with the previous instance of the same name

##########
# Task d #
##########

def posts_freq(data):
    # Returns a dict where key is fb_id and value is number of posts in feed
    dic = {}

    for post in data["feed"]["data"]:
        if(post["from"]["id"] not in dic):
            dic[post["from"]["id"]] = 1
        else:
            dic[post["from"]["id"]] += 1
    return dic

#print("Posts Frequency: ", posts_freq(fb_data))

##########
# Task e #
##########

def comments_freq(data):
    # Returns a dict where key is fb_id and value is number of comments in feed
    dic = {}

    for post in data["feed"]["data"]:
        if("comments" in post):
            for comment in post["comments"]["data"]:
                if(comment["from"]["id"] not in dic):
                    dic[comment["from"]["id"]] = 1
                else:
                    dic[comment["from"]["id"]] += 1
    return dic

#print("Comments Frequency: ", comments_freq(fb_data))

##########
# Task f #
##########

def likes_freq(data):
    # Returns a dict where key is fb_id and value is number of likes in feed
    dic = {}

    for post in data["feed"]["data"]:
        if("likes" in post):
            for like in post["likes"]["data"]:
                if(like["id"] not in dic):
                    dic[like["id"]] = 1
                else:
                    dic[like["id"]] += 1
    return dic

print("Likes Frequency: ", likes_freq(fb_data))

##########
# Task g #
##########

def popularity_score(data):
    # Returns a dict where key is fb_id and value is the number of likes
    # a person's posts and comments have
    dic = {}

    for post in data["feed"]["data"]:
        # Add wall post likes
        if("likes" in post):
            if(post["from"]["id"] not in dic):
                dic[post["from"]["id"]] = len(post["likes"]["data"])
            else:
                dic[post["from"]["id"]] += len(post["likes"]["data"])
                
        # Add comment likes
        if("comments" in post):
            for comment in post["comments"]["data"]:
                if(comment["like_count"] != 0):
                    if(comment["from"]["id"] not in dic):
                        dic[comment["from"]["id"]] = comment["like_count"]
                    else:
                        dic[comment["from"]["id"]] += comment["like_count"]
    return dic

#print("Popularity Score: ", popularity_score(fb_data))

##########
# Task h #
##########

def member_stats(data):
    # Expand the member dict to include the keys:
    # 'posts_count', 'comments_count' and 'likes_count'
    members = create_member_dict(data)
    posts = posts_freq(data)
    comments = comments_freq(data)
    likes = likes_freq(data)

    for member in members:
        if(member in posts):
            members[member]["posts_count"] = posts[member]
        else:
            members[member]["posts_count"] = 0
            
        if(member in comments):
            members[member]["comments_count"] = comments[member]
        else:
            members[member]["comments_count"] = 0
            
        if(member in likes):
            members[member]["likes_count"] = likes[member]
        else:
            members[member]["likes_count"] = 0

    return members
        

stats = member_stats(fb_data)
print(stats["10152805891837166"])

##########
# Task i #
##########

def activity_score(data):
    dic = {}
    stats = member_stats(data)

    for member in stats:
        dic[member] = stats[member]["posts_count"] * 3 + stats[member]["comments_count"] * 2 + stats[member]["likes_count"]

    return dic
    

scores = activity_score(fb_data)
# print(scores["10153020766393769"]) # => 30
# print(scores["857756387629369"]) # => 8


##########
# Task j #
##########

def active_members_of_type(data, k, type_fn):
    # This is a higher order function, where type is a function and
    # can be either posts_freq, comments_freq, likes_freq, etc
    # and filters out the pairs that have frequency >= k

    # Simple merge sort to sort by value
    def sort_val(lst):
        if(len(lst) <= 1):
            return lst

        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]
        sorted_left = sort_val(left)
        sorted_right = sort_val(right)

        return merge(sorted_left, sorted_right)

    def merge(left, right):
        result = []
        i = 0
        j = 0

        while(i < len(left) and j < len(right)):
            if(left[i][1] > right[j][1]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        
        return result

    # In-place insertion sort to sort segments with equal values by name
    def sort_name(lst):
        idx = 0
        while(idx < (len(lst) - 1)):
            # If current value not the same as next val, move forward
            if(lst[idx][1] != lst[idx + 1][1]):
                idx += 1
                    
            # Next val same as current
            else:
                curr_val = lst[idx][1]
                length = 1

                # Find where the sequence with same value extends till
                while(idx + length < len(lst) and lst[idx + length][1] == curr_val):
                    length += 1
                        
                for i in range(length):
                    min_term = lst[idx + i][0]
                    min_idx = idx + i
                    for j in range(1, length - i):
                        # Update smallest if necessary
                        if(lst[idx + i + j][0] < min_term):
                            min_term = lst[idx + i + j][0]
                            min_idx = idx + i + j
                    # Swap first element with smallest
                    lst[idx + i], lst[min_idx] = lst[min_idx], lst[idx + i]

                # Jump to next index after current block
                idx += length

        return lst                        

    """
    I saw that there is apparently a much better way of implementing the in-place insertion sort above:

    def sort_name_alt(lst):
        return sorted(lst, key=lambda x: (-x[1], x[0]))
    """
    
    
    members = create_member_dict(data)
    func_output = type_fn(data)

    output = []

    for id in func_output.keys():
        if(func_output[id] >= k):
            if(id in members):
                output.append([members[id]["name"], func_output[id]])
    output = sort_val(output)
    output = sort_name_l(output)
    return output


# print(active_members_of_type(fb_data, 2, posts_freq))

# print(active_members_of_type(fb_data, 20, comments_freq))

# print(active_members_of_type(fb_data, 40, likes_freq))

# print(active_members_of_type(fb_data, 20, popularity_score))

# print(active_members_of_type(fb_data, 80, activity_score))




########### DO NOT REMOVE THE TEST BELOW ###########

def gradeit():
    print("\n*** Facebook Stalker Autograding ***")
    print('==================')
    answers = json.loads(open('grading.json', 'r',  encoding='utf-8').read())
    total, correct = 0, 0
    def pass_or_fail(code, answer):
        nonlocal total
        total += 1
        if code == answer:
            nonlocal correct
            correct += 1
            return 'Passed!'
        else:
            return 'Failed.'
            
    print('Testing count_comments... ', pass_or_fail(count_comments(fb_data), answers['count_comments']))
    print('Testing count_likes... ', pass_or_fail(count_likes(fb_data), answers['count_likes']))
    print('Testing create_member_dict... ', pass_or_fail(create_member_dict(fb_data), answers['create_member_dict']))
    print('Testing posts_freq... ', pass_or_fail(posts_freq(fb_data), answers['posts_freq']))
    print('Testing comments_freq... ', pass_or_fail(comments_freq(fb_data), answers['comments_freq']))
    print('Testing likes_freq... ', pass_or_fail(likes_freq(fb_data), answers['likes_freq']))
    print('Testing popularity_score... ', pass_or_fail(popularity_score(fb_data), answers['popularity_score']))
    print('Testing member_stats... ', pass_or_fail(member_stats(fb_data), answers['member_stats']))
    print('Testing activity_score... ', pass_or_fail(activity_score(fb_data), answers['activity_score']))
    print('Testing members with >= 1 posts... ', pass_or_fail(active_members_of_type(fb_data, 1, posts_freq), answers['active_posters']))
    print('Testing members with >= 4 comments... ', pass_or_fail(active_members_of_type(fb_data, 4, comments_freq), answers['active_commenters']))
    print('Testing members with >= 4 likes... ', pass_or_fail(active_members_of_type(fb_data, 4, likes_freq), answers['active_likers']))
    print('Testing members who have >= 3 likes... ', pass_or_fail(active_members_of_type(fb_data, 3, popularity_score), answers['popular']))
    print('Testing members with an activity score of >= 10... ', pass_or_fail(active_members_of_type(fb_data, 10, activity_score), answers['overall_active']))
    print('==================')
    print('Grades: ' + str(correct) + '/' + str(total) + '\n')

gradeit()

        

