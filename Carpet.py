def solution(brown, yellow):
    total = brown + yellow
    answer = []

    for width in range(1,total+1):
        if total % width == 0:
            height = total//width
            if (2*width+2*height-4 == brown) and (width >= height):
                answer.append(width)
                answer.append(height)
    return answer
