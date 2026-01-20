
const tunebook = require('./abcjs_fork/src/api/abc_tunebook');

function testAbc(abc) {
    console.log("\n" + "=".repeat(40));
    console.log("Testing ABC:", abc.replace(/\n/g, "\\n"));
    console.log("=".repeat(40));
    try {
        const result = tunebook.parseOnly(abc);
        const tune = result[0];

        let foundNotes = [];
        tune.lines.forEach(line => {
            if (line.staff) {
                line.staff.forEach(staff => {
                    staff.voices.forEach(voice => {
                        voice.forEach(el => {
                            if (el.el_type === 'note' && (el.pitches || el.rest)) {
                                foundNotes.push(el);
                            }
                        });
                    });
                });
            }
        });

        foundNotes.forEach((el, i) => {
            const pitches = el.pitches || [];
            const info = pitches.map(p => {
                let s = p.name || 'rest';
                if (p.startSlur) s += ` (StartSlur: ${p.startSlur})`;
                if (p.endSlur) s += ` (EndSlur: ${p.endSlur})`;
                if (el.startSlur) s += ` (ElStartSlur: ${el.startSlur})`;
                if (el.endSlur) s += ` (ElEndSlur: ${el.endSlur})`;
                return s;
            }).join(', ');

            console.log(`Note ${i + 1}: ${info}`);
            if (el.gracenotes) {
                console.log(`  Gracenotes: ${el.gracenotes.map(g => g.name + (g.startSlur ? ' (startSlur)' : '') + (g.endSlur ? ' (endSlur)' : '')).join(', ')}`);
            }
        });
    } catch (e) {
        console.error("Error parsing ABC:", e);
    }
}

const cases = [
    "X:1\nK:G\nGAG ({BcB}G)AB", // Original case: slur before grace
    "X:1\nK:G\n(C(D)E)",         // Paul's Case 1: Nested slurs
    "X:1\nK:G\n(Cggg(D)gggE)",   // Paul's Case 2: Intervening notes
    "X:1\nK:G\n(C({g}D)E)",       // Paul's Case 3: Slur before grace + note
    "X:1\nK:HP\n({g}A)",         // Bagpipe case
    "X:1\nK:G\n{(cd)}e",         // Slur inside grace
    "X:1\nK:G\n{(cd}e)"          // Crossing boundary (the "hard" case)
];

cases.forEach(testAbc);
