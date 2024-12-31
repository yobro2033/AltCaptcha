async function hashMatch(t, e, r = "SHA-256", maxIterations = 1e6, start = 0) {
  const l = new AbortController();

  return new Promise((resolve, reject) => {
    const startTime = Date.now();

    const iterate = (iteration) => {
      if (l.signal.aborted || iteration > maxIterations) {
        resolve(null); // Return null if aborted or exceeded max iterations
      } else {
        generateHash(e, iteration, r)
          .then((computedHash) => {
            if (computedHash === t) {
              resolve({
                number: iteration,
                took: Date.now() - startTime,
              });
            } else {
              iterate(iteration + 1);
            }
          })
          .catch(reject);
      }
    };

    iterate(start);
  });
}

async function generateHash(data, iteration, algorithm) {
  return convertToHex(await crypto.subtle.digest(algorithm.toUpperCase(), textEncoder.encode(data + iteration)));
}

const textEncoder = new TextEncoder();

function convertToHex(buffer) {
  return [...new Uint8Array(buffer)]
    .map((byte) => byte.toString(16).padStart(2, "0"))
    .join("");
}

// Export the function for Node.js usage
module.exports = { hashMatch };
