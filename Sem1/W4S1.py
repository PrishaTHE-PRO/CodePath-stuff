# Problem 1: NFT Name Extractor
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - is every NFT represented as a dictionary containing a "name" key?
# - should the function return the NFT names in the same order they appear in the input list?

### P - Plan
# 2. Write out in plain English what you want to do:
# - create an empty list to store NFT names
# - iterate through each NFT dictionary in the collection
# - extract the value associated with the "name" key
# - add each name to the result list
# - return the completed list of NFT names

# 3. Translate each sub-problem into pseudocode:
# - create an emplty lsit called anmes
# - for each nft in nft_collection
    # - append nft["names"] to names
# - return names
# - O(n) and O(n)

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def extract_nft_names(nft_collection):
    names = []

    for nft in nft_collection:
        names.append(nft["name"])

    return names

# Problem 2: NFT Collection Review
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - what data type should the fucntion return: a list NFT names or a single string?
# - should the function handle an empty NFT collection by returning an empty list?

### P - Plan
# 2. Write out in plain English what you want to do:
# - review the existing code + determine bug
# - identify how += behaves in strings and lists
# - repalce the incorrect operation with one that adds each NFT as a single element to the result list
# - return the corrected list

# 3. Translate each sub-problem into pseudocode:
# - create an emoty list called nft_names
# - for each nft in nft_collection
    # - append nft["names"] to nft_names
# - return nft_names
# - O(n) and O(k)

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def extract_nft_names(nft_collection):
    nft_names = []

    for nft in nft_collection:
        nft_names.append(nft["name"])

    return nft_names

# Problem 3: Identify Popular Creators
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - WHat makes a creator "popular"?
# - should each creator appear only once in the output?

### P - Plan
# 2. Write out in plain English what you want to do:
# - count how many NFTs each creator has
# - return creators with more than one NFT

# 3. Translate each sub-problem into pseudocode:
# - create empty dict
# - for each nft in collection
# - set dict[creaotr] = 1
# - else increment 
# - create empty list
# - for each creator in dict
# - if dict[creator] > 1:
# - add creator to list
# - return list
# - O(n) and O(1)

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def identity_popular_creators(nft_collection):
    result = []
    count = {}

    for nft in nft_collection:
        count[nft["creator"]] = count.get(nft["creator"], 0) + 1

    for creator in count:
        if count[creator] > 1:
            result.append(creator)

        return result
    

# Problem 4: NFT Collection Statistics
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Which field should be used to calculate the everage?
# - what should be returned if the collection is empty?

### P - Plan
# 2. Write out in plain English what you want to do:
# - add up all NFT values
# - devide by the number of NFTs, or return 0 is there are none

# 3. Translate each sub-problem into pseudocode:
# - if nft_collection is empty:
# - return 0
# - set total = 0
# - for each nft in collection
# - total += nft["value"]
# - return total / length of nft_collection
# - O(n) and O(1)

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer
def average_nft_value(nft_collection):
    if not nft_collection:
        return 0
    total = 0
    for nft in nft_collection:
        total += nft["value"]
      
    return total/len(nft_collection) 

# Problem 5: NFT Tag Search
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - can an NFT belong to a nested collection of NFTs?
# - should all NFT names with the matching tag be returned?

### P - Plan
# 2. Write out in plain English what you want to do:
# - loop through each collection and NFT
# - add the NFT's name to the result if it contains the target tag

# 3. Translate each sub-problem into pseudocode:
# - create an empty list called result
# - for each collection in nft_collections
# - for each nft in collections
# - if tag is in nft["tags"]
# - add nft["name"] to result
# - return result

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def search_nft_by_tag(nft_collections, tag):
    result = []

    for collection in nft_collections:
        for nft in collection:
            if tag in nft["tags"]:
                result.append(nft["name"])

    return result
