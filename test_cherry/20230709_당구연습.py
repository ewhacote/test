def solution(m, n, startX, startY, balls):
    answer = []
    points = [[-startX, startY], [startX, -startY], [m * 2 - startX, startY], [startX, n * 2 - startY]]

    for x, y in balls:
        distance = []
        for pointX, pointY in points:
            ball_distance = (x - pointX) ** 2 + (y - pointY) ** 2
            start_distance = (startX - pointX) ** 2 + (startY - pointY) ** 2

            if not (startX == x == pointX or startY == y == pointY) or (ball_distance > start_distance):
                distance.append(ball_distance)
        answer.append(min(distance))

    return answer
