% include('header.tpl', title='NetDIMM Loader')

<div class="container">
	<nav class="navbar navbar-default" role="navigation">
		<div class="container-fluid">
			<div class="navbar-header">
				<button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
					<span class="sr-only">Toggle navigation</span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
				</button>
				<a class="navbar-brand">NetDIMM Loader</a>
			</div>
			
			<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
				<ul class="nav navbar-nav">
					<li class="active"><a href="#">Games</a></li>
					<li><a href="config">Configuration</a></li>
				</ul>
			</div>
		</div>
	</nav>
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