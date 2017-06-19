import lists.linkedlist as l


newlist = l.LinkList()

newlist.push(5)
newlist.push(6)
newlist.push(17)
newlist.push(10)

# print(newlist.out_put())
#
# print(newlist.headnode)
#
# print(newlist.traverse_to_end().next_node)
#
# newlist.pop()


print(newlist.traverse_to_end().value)

newlist.pop()

print(newlist.traverse_to_end().value)

newlist.ins(newlist.search(6),100)

newlist.out_put()
