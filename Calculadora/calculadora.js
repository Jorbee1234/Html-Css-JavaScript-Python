function limpar(){
	document.getElementById('visor').value='';
}
function preencher(valor){
	document.getElementById('visor').value+=valor;
}
function calcular(){
	var result=0;
	resultado=document.getElementById('visor').value;
	document.getElementById('visor').value=eval(resultado);
}