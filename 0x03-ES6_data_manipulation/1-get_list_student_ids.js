export default function getListStudentIds(listofObjects) {
  if (Array.isArray(listofObjects) === false) {
    return [];
  }
  const idList = listofObjects.map((x) => x.id);
  return idList;
}
