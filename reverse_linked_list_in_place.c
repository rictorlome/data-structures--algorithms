 /**
  * Reverse a list in place.
  * @param n1 - the pointer to the head of the original list. 
  * @return the pointer to the head of the reversed list.
  */
node* reverse(node* n1)
{
  node* prev = NULL;
  node* cur = &n1;
  node* aft = n1->next;
  while (cur != NULL)
  {
    cur->next = prev;
    prev = cur;
    cur = aft;
    if (aft != NULL)
    {
      aft = aft->next;
    }
  }
  return prev;
}
