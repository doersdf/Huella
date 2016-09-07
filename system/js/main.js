(function() {
	var indexScreen = document.getElementById('main'),
		riseUpScreen = document.getElementById('riseUp'),
		fingerprintScreen = document.getElementById('fingerprint'),
		codeScreen = document.getElementById('code'),
		inScreen = document.getElementById('in'),
		outScreen = document.getElementById('out'),
		errorScreen = document.getElementById('error'),
		statsScreen = document.getElementById('stats'),
		newuserScreen = document.getElementById('newuser');


	//INDEX
	indexScreen.addEventListener('click', function(){
		this.classList.add('hidden');
		codeScreen.classList.remove('hidden');
	});


	//CODE
	var codeNumbers = document.getElementsByClassName('number'),
		inputCode = document.querySelector('input.code');

	codeResult = "";

	for(var i = 0;  i < codeNumbers.length; i++) {
		codeNumbers[i].addEventListener('click', function(e){
			e.preventDefault();
			inputCode.value += "*";
			codeResult += this.value;
		});
	}

	document.getElementById('codeForm').addEventListener('submit', function(e) {
		e.preventDefault();
		if (codeResult === "1234") {
			codeScreen.classList.add('hidden');
			inScreen.classList.remove('hidden');
			this.reset();
		} else {
			codeScreen.classList.add('hidden');
			errorScreen.classList.remove('hidden');
			this.reset();
		}
	});


	//ERROR

	document.getElementById('backToIndex').addEventListener('click', function() {
		errorScreen.classList.add('hidden');
		indexScreen.classList.remove('hidden');
	});


	//SUCCESS 

	document.getElementById('showStats').addEventListener('click', function() {
		inScreen.classList.add('hidden');
		outScreen.classList.add('hidden');
		statsScreen.classList.remove('hidden');
	});

	//STATS

	document.getElementById('closeStats').addEventListener('click', function(){
		statsScreen.classList.add('hidden');
		riseUpScreen.classList.remove('hidden');
	});




})();