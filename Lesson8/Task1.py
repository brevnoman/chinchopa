def oops():
    l=[0]
    a=l[1]

def hop():
    try:
        oops()
    except IndexError:
        print("that list is not that large")

hop()

#
# def oops():
#     l={"pip": "install"}
#     a=l["install"]
#
# def hop():
#     try:
#         oops()
#     except KeyError:
#         print("This is incorrect key")
#
# hop()
