def draw_line(tick_length, tick_label=''):
    """Draw one line with given tick length followed by optional label"""
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)

def draw_interval(center_length):
    """Draw ticket interval based upon a central tick length"""
    if center_length > 0: # stop when length drops to zero
        draw_interval(center_length - 1) # recursively draw top ticks
        draw_line(center_length) # draw center tick
        draw_interval(center_length - 1) # recursively draw bottom ticks

def draw_ruler(num_inches, major_length):
    """Draw English rules with given number of inches, major tick length"""
    draw_line(major_length, '0') # draw inch 0 line
    for j in range(1, 1 + num_inches):
        draw_interval(major_length - 1) # draw interior ticks for inch
        draw_line(major_length, str(j)) # draw inch j line and label

if __name__ == '__main__':
    # num_inches = int(input("Enter the number of inches\n"))
    # major_length = int(input("Enter major length\n"))

    num_inches = 2
    major_length = 4

    draw_ruler(num_inches, major_length)
