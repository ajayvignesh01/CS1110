player_name = input("What player would you like to calculate statistics for? ")

opponent_team = input("What team was the opponent in the game you would like to calculate statistics for? ")

attempted_3s = input("How many 3's did " + player_name + " attempt this game? ")
made_3s = input("How many 3's did " + player_name + " make this game? ")

attempted_2s = input("How many 2's did " + player_name + " attempt this game? ")
made_2s = input("How many 2's did " + player_name + " make this game? ")

attempted_free_throws = input("How many free throws did " + player_name + " attempt this game? ")
made_free_throws = input("How many free throws did " + player_name + " make this game? ")


field_goal_made = int(made_3s) + int(made_2s)
field_goals_attempted = int(attempted_3s) + int(attempted_2s)
field_goal_percentage = field_goal_made/field_goals_attempted
field_goal_percentage_final = field_goal_percentage * 100


free_throw_made = int(made_free_throws)
free_throw_attempted = int(attempted_free_throws)
free_throw_percentage = free_throw_made/free_throw_attempted
free_throw_percentage_final = free_throw_percentage * 100

score_3s = int(made_3s) * 3
score_2s = int(made_2s) * 2
score_1s = int(made_free_throws) * 1
total_points = score_3s + score_2s + score_1s

print(player_name, "had a", str(field_goal_percentage_final) + "% field goal percentage and a", str(free_throw_percentage_final) + "% free throw percentage")
print(player_name + " scored", total_points, "points against " + opponent_team + ". Wahoowa!")