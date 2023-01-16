interface Student {
	firstName: string;
	lastName: string;
	age: number;
	location: string;
}

const student1: Student = {
  firstName: "Brayden",
  lastName: "Vernon",
  age: 23,
  location: "Tulsa"
}

const student2: Student = {
  firstName: "Tim",
  lastName: "Simms",
  age: 19,
  location: "Super-Cool-Ville"
}

const studentList: Array<Student> = [student1, student2];

const table = document.createElement('table');
studentList.forEach((student) => {
  const row = table.insertRow();
  const firstName = row.insertCell();
  const location = row.insertCell();
  firstName.innerHTML = student.firstName;
  location.innerHTML = student.location;
});

document.body.appendChild(table);
