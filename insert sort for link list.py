class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

def insertionSortList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    ehead = ListNode(x=0)
    ehead.next = head  # 前驱

    now = head
    nex = head.next
    ptr = ehead
    tail= now
    while now != None:

        if ptr.next == now:
            tail = now
            now=now.next
            ptr=ehead

            continue

        elif ptr.next.val > now.val:
            tail.next=now.next
            nex = now.next
            now.next = ptr.next
            ptr.next = now
            now = nex
            ptr = ehead
            continue
        ptr = ptr.next
    return ehead.next


val=[4,2,1,3]
for i in range(len(val)):
    if i ==0:
        head=ListNode(x=val[0])
        node=head
    else:
        node.next=ListNode(x=val[i])
        node=node.next

node.next=None

ehead=insertionSortList(head)

while head!=None:
    print(head.val)
    head=head.next