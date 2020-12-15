# src/...
import re


def loadbags(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    return lines


def createdict(lines):
    dict = {}
    bag_and_contents_regex = r"^(\w+ \w+) bags contain (.*)"
    contents_regex = r"([0-9] )*(\w+ \w+) bag"
    for item in lines:
        bag_and_contents = re.search(bag_and_contents_regex, item)
        bag_type = bag_and_contents[1]
        contents_string = bag_and_contents[2][:-1]  # [:-1] removes trailing period
        contents_tuples = re.findall(contents_regex, contents_string)

        bag_contents = []
        for contents_tuple in contents_tuples:
            if contents_tuple[1] != "no other":
                bag_contents.append(
                    {"count": int(contents_tuple[0]), "type": contents_tuple[1]}
                )
        dict[bag_type] = bag_contents

    return dict


def countcertainbag(bagdict, bagname, lookfor):
    count = 0
    bag = bagdict[bagname]

    if len(bag) != 0:
        for baginbag in bag:
            if baginbag["type"] == lookfor:
                count += 1
            count += countcertainbag(bagdict, baginbag["type"], lookfor)
    return count


def bagscontainingbag(bagdict, lookfor):
    bagnamelist = []
    for bagname in bagdict.keys():
        if countcertainbag(bagdict, bagname, lookfor) > 0:
            bagnamelist.append(bagname)
    return bagnamelist


def bag_count(bagdict, bag_name):
    count = 0
    top_bag = bagdict[bag_name]

    if len(top_bag) != 0:
        for this_bag in top_bag:
            count += this_bag["count"]
            count += bag_count(bagdict, this_bag["type"]) * this_bag["count"]

    return count


lines = loadbags("dec07_input.txt")
bagdict = createdict(lines)
haveshinygold = bagscontainingbag(bagdict, "shiny gold")

print(haveshinygold)
print(len(haveshinygold))

inshinygold = bag_count(bagdict, "shiny gold")

print(inshinygold)
