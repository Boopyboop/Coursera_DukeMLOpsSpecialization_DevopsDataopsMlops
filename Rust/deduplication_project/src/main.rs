 use std::collections::HashSet;

/// Entry point of the program.
/// Applies deduplication on a hardcoded list of strings.
fn main() {
    let items = vec![
        String::from("apple"),
        String::from("banana"),
        String::from("apple"),
        String::from("orange"),
        String::from("banana"),
    ];

    let unique_items = deduplicate(items);

    println!("Unique items: {:?}", unique_items);
}

/// Removes duplicate strings from a vector.
///
/// # Arguments
/// * `items` - A vector of strings, possibly with duplicates.
///
/// # Returns
/// A vector of unique strings (order not guaranteed).
///
/// # Examples
/// ```
/// let data = vec![
///     String::from("a"),
///     String::from("b"),
///     String::from("a")
/// ];
/// let result = deduplication_tool::deduplicate(data);
/// assert_eq!(result.len(), 2);
/// ```
pub fn deduplicate(items: Vec<String>) -> Vec<String> {
    let set: HashSet<String> = items.into_iter().collect();
    set.into_iter().collect()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_deduplicate_with_duplicates() {
        let input = vec![
            String::from("apple"),
            String::from("banana"),
            String::from("apple"),
        ];
        let result = deduplicate(input);
        assert_eq!(result.len(), 2);
    }

    #[test]
    fn test_deduplicate_no_duplicates() {
        let input = vec![
            String::from("apple"),
            String::from("banana"),
            String::from("orange"),
        ];
        let result = deduplicate(input.clone());
        assert_eq!(result.len(), input.len());
    }

    #[test]
    fn test_deduplicate_empty() {
        let input: Vec<String> = vec![];
        let result = deduplicate(input);
        assert_eq!(result.len(), 0);
    }
}
