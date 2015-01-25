% include('header.tpl', title='NetDIMM Loader')

<div class="container">
	% include('navbar.tpl', activePage='games')
	
	% if defined('games'):
	<p>Choose a game to play</p>
	% for game in games:
		<p>
			<a href="load/{{game.__hash__()}}">{{game.name[region]}}</a> <span class="label label-default">{{round(game.size/float(1024*1024), 1)}} MB</span>
		</p>
	% end
	% end

	% if not defined('games'):
	<div class="alert alert-danger"><span class="glyphicon glyphicon-warning-sign"></span> No games were found! Verify that the directory set on the configuration screen exists and contains valid NAOMI games.</div>
	% end

</div>

% include('footer.tpl')
