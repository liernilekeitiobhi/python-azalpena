let pyodideReady = false;
let pyodide = null;

async function initPyodide() {
    pyodide = await loadPyodide();
    await pyodide.loadPackage("micropip");
    pyodideReady = true;
    document.querySelectorAll('.run-code').forEach(btn => {
        btn.disabled = false;
        btn.textContent = "Run Python";
    });
}

function getActualCode(element) {
    const codeElement = element.querySelector('.code pre code');
    if (!codeElement) return null;
    const clone = codeElement.cloneNode(true);
    clone.querySelectorAll('.lineno, .normal').forEach(el => el.remove());
    return clone.textContent;
}

document.addEventListener("DOMContentLoaded", function() {
    initPyodide();
    
    document.querySelectorAll('div.language-python.highlight').forEach(function(block) {
        const button = document.createElement("button");
        button.className = "run-code";
        button.textContent = "Loading Pyodide...";
        button.disabled = true;
        
        const output = document.createElement("div");
        output.className = "execution-output";
        output.style.display = "none";
        
        block.parentNode.insertBefore(button, block.nextSibling);
        block.parentNode.insertBefore(output, button.nextSibling);
        
        button.addEventListener("click", async function() {
            if (!pyodideReady) {
                output.textContent = "Python is still loading...";
                output.style.display = "block";
                return;
            }
            
            button.disabled = true;
            button.textContent = "Running...";
            output.textContent = "Executing...";
            output.style.display = "block";
            
            try {
                const code = getActualCode(block);
                if (!code) throw new Error("Could not extract code");
                
                // Create a Python function to capture print output
                const wrappedCode = `
import sys
from io import StringIO
old_stdout = sys.stdout
sys.stdout = mystdout = StringIO()
try:
${code.split('\n').map(line => `    ${line}`).join('\n')}
finally:
    sys.stdout = old_stdout
mystdout.getvalue()
`;
                
                const result = await pyodide.runPythonAsync(wrappedCode);
                output.textContent = result || "Code executed (no output)";
            } catch (err) {
                output.textContent = "Error: " + err.message;
                console.error(err);
            } finally {
                button.disabled = false;
                button.textContent = "Run Again";
            }
        });
    });
});