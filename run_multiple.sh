#!/usr/bin/env bash
#for run in {1..5}
#do
#    python tournament.py
#done

echo "Running heuristic: heuristic_score_player_moves"
touch result/heuristic_score_player_moves.txt
python tournament.py heuristic_score_player_moves >> result/heuristic_score_player_moves.txt


echo "Running heuristic: heuristic_score_normal_difference_moves"
touch result/heuristic_score_normal_difference_moves.txt
python tournament.py heuristic_score_normal_difference_moves >> result/heuristic_score_normal_difference_moves.txt


echo "Running heuristic: heuristic_score_quadratic_difference_moves"
touch result/heuristic_score_quadratic_difference_moves.txt
python tournament.py heuristic_score_quadratic_difference_moves >> result/heuristic_score_quadratic_difference_moves.txt



echo "Running heuristic: heuristic_score_final_custom_score"
touch result/heuristic_score_final_custom_score.txt
python tournament.py heuristic_score_final_custom_score >> result/heuristic_score_final_custom_score.txt