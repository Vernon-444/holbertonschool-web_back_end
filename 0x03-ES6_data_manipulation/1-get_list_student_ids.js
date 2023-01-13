export default function getListStudentIds(listofObjects) {
  if (Array.isArray(listofObjects) === false) {
    return [];
  }
  const id_list = listofObjects.map((x) => x.id);
  return id_list;
}
