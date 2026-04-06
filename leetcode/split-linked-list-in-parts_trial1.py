class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
       
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        part_size = n // k
        extra = n % k

        res = []
        cur = head

        for i in range(k):
            res.append(cur)
            size = part_size + (1 if i < extra else 0)

            for _ in range(size - 1):
                if cur:
                    cur = cur.next

            if cur:
                nxt = cur.next
                cur.next = None
                cur = nxt

        return res