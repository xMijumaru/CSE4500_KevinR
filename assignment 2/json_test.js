//this part will cover json.parse()

var data = '{"people":[{"name": "person1", "city": "city1"}, {"name":"person2", "city":"city2"}]} ';
console.log(JSON.parse(data).people[0].name);

//this part will cover json.stringify()

var testobj = {name: "kevin", age: 22, city: "san bernardino"};
console.log(JSON.stringify(testobj));