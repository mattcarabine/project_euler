%%%-------------------------------------------------------------------
%%% @author matt
%%% @copyright (C) 2018, <COMPANY>
%%% @doc
%%%
%%% @end
%%% Created : 11. Jun 2018 00:41
%%%-------------------------------------------------------------------
-module(problem1).
-author("matt").

%% API
-export([main/0]).
main () ->
  lists:sum([X || X <- lists:seq(1,999), multiple(X)]).

multiple(X) ->
  (X rem 3 =:= 0) or (X rem 5 =:= 0).
