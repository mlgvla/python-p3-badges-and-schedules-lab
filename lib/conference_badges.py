def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [badge_maker(name) for name in names]

def assign_rooms(names):
    return [f"Hello, {item}! You'll be assigned to room {index + 1}!" for index, item in enumerate(names)]

def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)
    
    for room_assignment in assign_rooms(names):
        print(room_assignment)
    
