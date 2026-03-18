import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 스택 그리기 함수
def draw_stack(stack, message=""):
    plt.clf()
    plt.title("Stack Animation", fontsize=15)

    # 메시지
    plt.text(-2, len(stack)+1, message, fontsize=12)

    # 스택 그리기
    for i, item in enumerate(stack):
        plt.gca().add_patch(plt.Rectangle((0, i), 2, 1, fill=False))
        plt.text(1, i+0.5, item, ha='center', va='center')

    # top 표시
    if stack:
        plt.text(2.5, len(stack)-0.5, "← TOP", fontsize=12)

    plt.xlim(-2, 4)
    plt.ylim(0, 10)
    plt.axis('off')
    plt.pause(1)

# ===== 시작 =====
stack = []
plt.figure()

# push
words = ["벚꽃", "버터떡", "두쫀쿠", "중간고사", "딸기라떼", "카공"]

for w in words:
    stack.append(w)
    draw_stack(stack, f"push: {w}")

# top
draw_stack(stack, f"top: {stack[-1]}")

# pop
stack.pop()
draw_stack(stack, "pop")

# 추가 push (남은 키워드)
more_words = ["말차", "아아", "핑크색", "커피"]

for w in more_words:
    stack.append(w)
    draw_stack(stack, f"push: {w}")

plt.show()