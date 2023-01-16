var student1 = {
    firstName: "Brayden",
    lastName: "Vernon",
    age: 23,
    location: "Tulsa"
};
var student2 = {
    firstName: "Tim",
    lastName: "Simms",
    age: 19,
    location: "Super-Cool-Ville"
};
var studentList = [student1, student2];
var table = document.createElement('table');
studentList.forEach(function (student) {
    var row = table.insertRow();
    var firstName = row.insertCell();
    var location = row.insertCell();
    firstName.innerHTML = student.firstName;
    location.innerHTML = student.location;
});
document.body.appendChild(table);
