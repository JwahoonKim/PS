def distribute(seller, amount, referral_dict):
    if amount == 0:
        return

    referral_dict[seller][1] += amount - int((amount / 10))
    referral, _ = referral_dict[seller]
    if referral == '-':
        return

    distribute(referral, int(amount / 10), referral_dict)


def solution(enroll, referral, seller, amount):
    referral_dict = dict()
    for me, refer in zip(enroll, referral):
        referral_dict[me] = [refer, 0]

    seller_info = []
    for s, a in zip(seller, amount):
        seller_info.append([s, a * 100])

    for s, a in seller_info:
        distribute(s, a, referral_dict)

    answer = []
    for e in enroll:
        answer.append(referral_dict[e][1])

    return answer


enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

solution(enroll, referral, seller, amount)