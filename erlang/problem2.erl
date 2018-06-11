%%%-------------------------------------------------------------------
%%% @author matt
%%% @copyright (C) 2018, <COMPANY>
%%% @doc
%%%
%%% @end
%%% Created : 11. Jun 2018 01:22
%%%-------------------------------------------------------------------
-module(problem2).
-author("matt").

%% API
-export([main/0]).

main() ->
  lists:sum(lists:filter(fun(E) -> (E rem 2 =:= 0) andalso (E < 4000000) end, fib(100))).

fib(N) ->
    fib(N, 0, 1, []).
fib(0, _Current, _Next, Fibs) ->
    lists:reverse(Fibs);
fib(N, Current, Next, Fibs) ->
    fib(N - 1, Next, Current + Next, [Current|Fibs]).


