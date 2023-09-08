/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function(ransomNote, magazine) {
    let arrMagazine = magazine.split("")
    let arrRansomeNote = ransomNote.split("")

    for (let ltr of arrRansomeNote){
        console.log("Letter:", ltr)
        if (arrMagazine.includes(ltr)){
            console.log("arrMagazine pre-cut", arrMagazine)
            console.log("arrRansomeNote pre-cut", arrRansomeNote)
            // arrRansomeNote.splice(arrRansomeNote.indexOf(ltr), 1);
            arrMagazine.splice(arrMagazine.indexOf(ltr), 1);
            console.log("arrMagazine post-cut", arrMagazine)
            console.log("arrRansomeNote post-cut", arrRansomeNote)
        } else {
            return false;
        }
    }
    return true;
    // if (arrRansomeNote.length === 0) {
    //     return true
    // } else {
    //     return false
    // }
};