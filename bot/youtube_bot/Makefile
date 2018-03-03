# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fbenneto <fbenneto@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/11/25 19:25:27 by fbenneto          #+#    #+#              #
#    Updated: 2017/11/25 19:36:48 by fbenneto         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

YOUTUBE_DL = "youtube-dl"
G_AUTH = "google-auth"
G_OAUTH_LIB = "google-auth-oauthlib"
G_OAUTH_HTTPLIB2 = "google-auth-httplib2"

YEL="\\033[33m"
BLU="\\033[34m"
RED="\\033[31m"
NC="\\033[0m"
MAG="\\033[35m"
CYA="\\033[36m"
GRE="\\033[32m"
BOL="\\033[1m"
CHE="\\xE2\\x9C\\x94"
OK="$(GRE)$(CHE)$(NC)"


all: $(YOUTUBE_DL) $(G_AUTH) $(G_OAUTH_LIB) $(G_OAUTH_HTTPLIB2)

$(YOUTUBE_DL):
	@printf "doing pip $(BOL)$(CYA)$@$(NC)"
	@pip install --upgrade $@
	@printf '\t\t'$(OK)'\n'

$(G_AUTH):
	@printf "doing pip $(BOL)$(CYA)$@$(NC)"
	@pip install --upgrade $@
	@printf '\t\t'$(OK)'\n'

$(G_OAUTH_LIB):
	@printf "doing pip $(BOL)$(CYA)$@$(NC)"
	@pip install --upgrade $@
	@printf '\t'$(OK)'\n'

$(G_OAUTH_HTTPLIB2):
	@printf "doing pip $(BOL)$(CYA)$@$(NC)"
	@pip install --upgrade $@
	@printf '\t'$(OK)'\n'
