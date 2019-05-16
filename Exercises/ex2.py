from container import *


def banana_verify(source_w, goal_w, cont: object, move_list: list):
    '''
    (str, str, obj, list) -> bool
    '''
    goal_word = ''
    for i in move_list:
        if i == 'P':
            if len(source_w) != 0:
                cont.put(source_w[0])
                source_w = source_w[1:]
        elif i == 'M':
            if len(source_w) != 0:
                goal_word += source_w[0]
                source_w = source_w[1:]
        else:
            get = cont.get()
            goal_word += get[0]
            # get = get[1:]

    return goal_word == goal_w

if __name__ == "__main__":
    BANANA = "BANANA"
    sorce_word = ["BNAAAN", "NBNAAA", "NNBAAA", "ANANAB", "NABANA"]
    print(banana_verify(BANANA, 'AAANNB', Stack(), list("PMPMPMGGG")))
    print(banana_verify(BANANA, 'BNAAAN', Stack(), list("MPMMGPMG")))
    print(banana_verify(BANANA, 'NBNAAA', Queue(), list("PPMGPMMGG")))
    print(banana_verify(BANANA, 'NNAAAB', Stack(), list("PPMPMGGMG")))
    print(banana_verify(BANANA, 'NNBAAA', Queue(), list("PPMPMGGGM")))
    print(banana_verify(BANANA, 'ANANAB', Stack(), list("PPPPPMGGGGG")))
    print(banana_verify(BANANA, 'NABANA', Stack(), list("PPMGGMMM")))

# 1
# impossible
# 2
# Stack
# Stack put(B) move(A) put(N) move(A) put(N)
#  move(A) get() get() get() PMPMPMGGG
# 3
# stack
# stack move(B) put(A) move(N) move(A) get()
#  put(N) move(A) get() MPMMGPMG
# 4
# queue
# queue put(B) put(A) move(N) get() put(A)
#  move(N) move(A) get() get() PPMGPMMGG
# 5
# stack
# stack put(B) put(A) move(N) put(A) move(B)
#  get() get() move(A) get() PPMPMGGMG
# 6
# queue
# queue put(B) put(A) move(N) put(A) move(N)
#  get() get() get() move(A) PPMPMGGGM
# 7
# stack
# stack put(B) put(A) put(N) put(A) put(N)
#  move(A) get() get() get() get() get() PPPPPMGGGGG
# 8
# stack
# stack put(B) put(A) move(N) get() get()
#  move(A) move(N) move(A) PPMGGMMM
# 9
# impossible
