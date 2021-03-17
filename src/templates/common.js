<script>

const cyrb53 = function(str, seed = 0) {
    let h1 = 0xdeadbeef ^ seed, h2 = 0x41c6ce57 ^ seed;
    for (let i = 0, ch; i < str.length; i++) {
        ch = str.charCodeAt(i);
        h1 = Math.imul(h1 ^ ch, 2654435761);
        h2 = Math.imul(h2 ^ ch, 1597334677);
    }
    h1 = Math.imul(h1 ^ (h1>>>16), 2246822507) ^ Math.imul(h2 ^ (h2>>>13), 3266489909);
    h2 = Math.imul(h2 ^ (h2>>>16), 2246822507) ^ Math.imul(h1 ^ (h1>>>13), 3266489909);
    return 4294967296 * (2097151 & h2) + (h1>>>0);
};
function getLastHash(){
	$.ajax({
		type:'POST',
		async:false,
		url:'http://127.0.0.1:5000/api/findhashByFileName',
		data: $('form').serialize(),
		dataType:'json',
		success:function(res){
			lastHash=res[0]['hash'];
			alert("Last Hash: "+lastHash);
		}
	});
}
function updateToCurrentHash(){
	alert("Change");
	/*{'search':{'fileName': 'demo'}, 'hash': ''}*/
	$.ajax({
		type:'POST',
		url: 'http://127.0.0.1:5000/api/filetrackAJAX',
		async: false,
		//data: {"search":{"fileName": "demo"}, "hash": hash},
		data: $('form').serialize(),
		dataType:'json',
		success:function(res){
			alert(JSON.stringify(res));
			var updatedHash = res[0]['hash'];
			if(updatedHash==currentHash){
				alert("Hash Value updated successfully");
			}else{
				alert("ERROR")
			}

		}
	});
}
</script>