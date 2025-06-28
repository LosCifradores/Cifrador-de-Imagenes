# Cifrador de Imágenes Salsa20: Acuerdos de trabajo

En el presente documento se detallan los acuerdos de trabajo para el desarrollo del backend de la aplicación de prestadores.

## Git

Se utilizará un modelo simplificado de workflow en base al planteado por **Vincent Driessen**, en https://nvie.com/posts/a-successful-git-branching-model/.
Se utilizará una ramas principal: **_main_** y ramas **_feature_** para el desarrollo de nuevas funcionalidades.

### Utilizacion de las ramas:
- **Main**: será la rama de origen, aquí se encuentra el código listo para la utilización del usuario (producción).
- **Feature**: en estas ramas es donde se modificará el código, nacen de main con el fin de añadir o cambiar alguna funcionalidad.  Las nombraremos con una breve descripción del feature. Una vez completado el trabajo se hará merge a main y se elimina la rama feature.

### Git rebase:
Luego que un desarrollador termine el feature en el que estaba trabajando y antes de solicitar el *peer review*, debe adaptar estos cambios a la rama de destino en caso de que esta esté adelantada a su trabajo. Esto se realiza con un `rebase`. Esto permite que el historial de commits se vea más limpio, ya que luego de realizado el merge, se visualizará como si la rama del nuevo feature saliera del último commit de la rama destino.

Al hacer esto, si efectivamente el `git rebase` produce cambios en nuestra historia, git no estará muy contento de subir esos cambios, y nos pedirá que use la opción `--force` con cuidado para pisar la historia (ATENCIÓN: siempre estamos hablando de nuestro feature branch).

#### Force: git push --force

> Imagine that you have to rebase what you have already published. You will have to bypass the "must fast-forward" rule in order to replace the history you originally published with the rebased history. If somebody else built on top of your original history while you are rebasing, the tip of the branch at the remote may advance with her commit, and blindly pushing with --force will lose her work.

Al hacer esto, si la feature branch sufrió modificaciones (por ejemplo alguien que colabora con nosotros subió una corrección de algún tema), la opción --force sobreescribiría sus cambios con los nuestros. Por eso, una opción un poco más segura es `--force-with-lease`.

#### Force con responsabilidad: git push --force-with-lease

> This option allows you to say that you expect the history you are updating is what you rebased and want to replace. If the remote ref still points at the commit you specified, you can be sure that no other people did anything to the ref. It is like taking a "lease" on the ref without explicitly locking it, and the remote ref is updated only if the "lease" is still valid.

> Is a safer option than --force because it will not overwrite any work on the remote branch if more commits were added to the remote branch (by another team-member or coworker or what have you). It ensures you do not overwrite someone elses work by force pushing.
